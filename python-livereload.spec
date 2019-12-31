#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	LiveReload - tool for web developers
Summary(pl.UTF-8):	LiveReload - narzędzie dla programistów WWW
Name:		python-livereload
Version:	2.6.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/livereload/
Source0:	https://files.pythonhosted.org/packages/source/l/livereload/livereload-%{version}.tar.gz
# Source0-md5:	7d155b74421b96a265f291404368d0da
URL:		https://github.com/lepture/python-livereload
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python LiveReload is an awesome tool for web developers.

%description -l pl.UTF-8
Python LiveReload jest niesamowitym narzędziem dla programistów WWW.

%package -n python3-livereload
Summary:	LiveReload - tool for web developers
Summary(pl.UTF-8):	LiveReload - narzędzie dla programistów WWW
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
Conflicts:	python-livereload < 2.6.1

%description -n python3-livereload
Python LiveReload is an awesome tool for web developers.

%description -n python3-livereload -l pl.UTF-8
Python LiveReload jest niesamowitym narzędziem dla programistów WWW.

%prep
%setup -q -n livereload-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/livereload{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/livereload{,-3}
ln -s livereload-3 $RPM_BUILD_ROOT%{_bindir}/livereload
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/livereload-2
%{py_sitescriptdir}/livereload
%{py_sitescriptdir}/livereload-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-livereload
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/livereload
%attr(755,root,root) %{_bindir}/livereload-3
%{py3_sitescriptdir}/livereload
%{py3_sitescriptdir}/livereload-%{version}-py*.egg-info
%endif
