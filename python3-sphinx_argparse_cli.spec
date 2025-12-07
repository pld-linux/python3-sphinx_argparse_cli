#
# Conditional build:
%bcond_with	tests	# unit tests

Summary:	Render CLI arguments (sub-commands friendly) defined by argparse module
Summary(pl.UTF-8):	Renderowanie argumentów CLI (z obsługą podpoleceń) definiowanych przez moduł argparse
Name:		python3-sphinx_argparse_cli
Version:	1.20.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-argparse-cli/sphinx_argparse_cli-%{version}.tar.gz
# Source0-md5:	fa87c89aacf32b654e0bf5a6b79b6c16
URL:		https://pypi.org/project/sphinx-argparse-cli/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs >= 0.5
BuildRequires:	python3-hatchling >= 1.27
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
%if %{with tests}
BuildRequires:	python3-Sphinx >= 8.2.3
BuildRequires:	python3-defusedxml >= 0.7.1
BuildRequires:	python3-pytest >= 8.4.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Render CLI arguments (sub-commands friendly) defined by the argparse
module. For live demo checkout the documentation of tox, pypa-build
and mdpo.

%description -l pl.UTF-8
Renderowanie argumentów CLI (z obsługą podpoleceń) definiowanych przez
moduł argparse. Na żywo efekt można zobaczyć w dokumentacji pakietów
tox, pypa-build i mdpo.

%prep
%setup -q -n sphinx_argparse_cli-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
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
