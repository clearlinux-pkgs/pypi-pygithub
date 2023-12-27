#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pygithub
Version  : 2.1.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/e2/bc/b9a3c3d6870d1e216fa8c79cf6d183a2da3df1bdcb7823c79cd2a6faa6b6/PyGithub-2.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/bc/b9a3c3d6870d1e216fa8c79cf6d183a2da3df1bdcb7823c79cd2a6faa6b6/PyGithub-2.1.1.tar.gz
Summary  : Use the full Github API v3
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0 MIT
Requires: pypi-pygithub-license = %{version}-%{release}
Requires: pypi-pygithub-python = %{version}-%{release}
Requires: pypi-pygithub-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(requests)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PyGitHub
[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/PyGithub)
![CI](https://github.com/PyGithub/PyGithub/workflows/CI/badge.svg)
[![readthedocs](https://img.shields.io/badge/docs-stable-brightgreen.svg?style=flat)](https://pygithub.readthedocs.io/en/stable/?badge=stable)
[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
[![Slack](https://img.shields.io/badge/Slack%20channel-%20%20-blue.svg)](https://join.slack.com/t/pygithub-project/shared_invite/zt-duj89xtx-uKFZtgAg209o6Vweqm8xeQ)
[![Open Source Helpers](https://www.codetriage.com/pygithub/pygithub/badges/users.svg)](https://www.codetriage.com/pygithub/pygithub)
[![codecov](https://codecov.io/gh/PyGithub/PyGithub/branch/master/graph/badge.svg)](https://codecov.io/gh/PyGithub/PyGithub)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

%package license
Summary: license components for the pypi-pygithub package.
Group: Default

%description license
license components for the pypi-pygithub package.


%package python
Summary: python components for the pypi-pygithub package.
Group: Default
Requires: pypi-pygithub-python3 = %{version}-%{release}

%description python
python components for the pypi-pygithub package.


%package python3
Summary: python3 components for the pypi-pygithub package.
Group: Default
Requires: python3-core
Provides: pypi(pygithub)
Requires: pypi(deprecated)
Requires: pypi(pyjwt)
Requires: pypi(pynacl)
Requires: pypi(python_dateutil)
Requires: pypi(requests)
Requires: pypi(typing_extensions)
Requires: pypi(urllib3)

%description python3
python3 components for the pypi-pygithub package.


%prep
%setup -q -n PyGithub-2.1.1
cd %{_builddir}/PyGithub-2.1.1
pushd ..
cp -a PyGithub-2.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696262516
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pygithub
cp %{_builddir}/PyGithub-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-pygithub/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/PyGithub-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pypi-pygithub/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/PyGithub-%{version}/tests/ReplayData/Github.testGetLicense.txt %{buildroot}/usr/share/package-licenses/pypi-pygithub/c93f43ee82da36b091a1f6b03cd3acd4ca2b2c0d || :
cp %{_builddir}/PyGithub-%{version}/tests/ReplayData/License.setUp.txt %{buildroot}/usr/share/package-licenses/pypi-pygithub/519e6fe35ab02fbdbd4b9fba86485f8a2f709906 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pygithub/519e6fe35ab02fbdbd4b9fba86485f8a2f709906
/usr/share/package-licenses/pypi-pygithub/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/pypi-pygithub/c93f43ee82da36b091a1f6b03cd3acd4ca2b2c0d
/usr/share/package-licenses/pypi-pygithub/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
