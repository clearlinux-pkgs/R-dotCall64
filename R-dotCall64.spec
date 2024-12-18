#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-dotCall64
Version  : 1.2
Release  : 58
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/dotCall64_1.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/dotCall64_1.2.tar.gz
Summary  : Enhanced Foreign Function Interface Supporting Long Vectors
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dotCall64-lib = %{version}-%{release}
BuildRequires : R-RhpcBLASctl
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and .Fortran() from the foreign function interface. .C64() supports long
    vectors, arguments of type 64-bit integer, and provides a mechanism to
    avoid unnecessary copies of read-only and write-only arguments. This
    makes it a convenient and fast interface to C/C++ and Fortran code.

%package dev
Summary: dev components for the R-dotCall64 package.
Group: Development
Requires: R-dotCall64-lib = %{version}-%{release}
Provides: R-dotCall64-devel = %{version}-%{release}
Requires: R-dotCall64 = %{version}-%{release}

%description dev
dev components for the R-dotCall64 package.


%package lib
Summary: lib components for the R-dotCall64 package.
Group: Libraries

%description lib
lib components for the R-dotCall64 package.


%prep
%setup -q -n dotCall64
pushd ..
cp -a dotCall64 buildavx2
popd
pushd ..
cp -a dotCall64 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731639479

%install
export SOURCE_DATE_EPOCH=1731639479
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dotCall64/CITATION
/usr/lib64/R/library/dotCall64/DESCRIPTION
/usr/lib64/R/library/dotCall64/INDEX
/usr/lib64/R/library/dotCall64/Meta/Rd.rds
/usr/lib64/R/library/dotCall64/Meta/features.rds
/usr/lib64/R/library/dotCall64/Meta/hsearch.rds
/usr/lib64/R/library/dotCall64/Meta/links.rds
/usr/lib64/R/library/dotCall64/Meta/nsInfo.rds
/usr/lib64/R/library/dotCall64/Meta/package.rds
/usr/lib64/R/library/dotCall64/NAMESPACE
/usr/lib64/R/library/dotCall64/NEWS
/usr/lib64/R/library/dotCall64/R/dotCall64
/usr/lib64/R/library/dotCall64/R/dotCall64.rdb
/usr/lib64/R/library/dotCall64/R/dotCall64.rdx
/usr/lib64/R/library/dotCall64/help/AnIndex
/usr/lib64/R/library/dotCall64/help/aliases.rds
/usr/lib64/R/library/dotCall64/help/dotCall64.rdb
/usr/lib64/R/library/dotCall64/help/dotCall64.rdx
/usr/lib64/R/library/dotCall64/help/paths.rds
/usr/lib64/R/library/dotCall64/html/00Index.html
/usr/lib64/R/library/dotCall64/html/R.css
/usr/lib64/R/library/dotCall64/tests/run-all.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-againstDotC.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-center.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-left.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-right.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-long_int64.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-vector_dc.R

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/dotCall64/include/dotCall64.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/dotCall64/libs/dotCall64.so
/V4/usr/lib64/R/library/dotCall64/libs/dotCall64.so
/usr/lib64/R/library/dotCall64/libs/dotCall64.so
