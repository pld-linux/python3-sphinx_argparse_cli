#
# Conditional build:
%bcond_with	tests	# unit tests

Summary:	Render CLI arguments (sub-commands friendly) defined by argparse module
Name:		python3-sphinx_argparse_cli
Version:	1.19.0
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-argparse-cli/sphinx_argparse_cli-%{version}.tar.gz
# Source0-md5:	c7c642b6e709d25b376773903d0df71a
URL:		https://pypi.org/project/sphinx-argparse-cli/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.2.0
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
Conflicts:	python3-commonmark < 0.5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Render CLI arguments (sub-commands friendly) defined by the argparse
module. For live demo checkout the documentation of tox, pypa-build
and mdpo.

%prep
%setup -q -n sphinx_argparse_cli-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py3_sitescriptdir}/sphinx_argparse_cli
%{py3_sitescriptdir}/sphinx_argparse_cli-%{version}.dist-info
