#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dotCall64
Version  : 1.0.1
Release  : 35
URL      : https://cran.r-project.org/src/contrib/dotCall64_1.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dotCall64_1.0-1.tar.gz
Summary  : Enhanced Foreign Function Interface Supporting Long Vectors
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dotCall64-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
and .Fortran() from the foreign function interface. .C64() supports long
    vectors, arguments of type 64-bit integer, and provides a mechanism to
    avoid unnecessary copies of read-only and write-only arguments. This
    makes it a convenient and fast interface to C/C++ and Fortran code.

%package lib
Summary: lib components for the R-dotCall64 package.
Group: Libraries

%description lib
lib components for the R-dotCall64 package.


%prep
%setup -q -c -n dotCall64
cd %{_builddir}/dotCall64

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613145022

%install
export SOURCE_DATE_EPOCH=1613145022
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dotCall64
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dotCall64
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dotCall64
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dotCall64 || :


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
/usr/lib64/R/library/dotCall64/include/dotCall64.h
/usr/lib64/R/library/dotCall64/tests/run-all.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-againstDotC.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-center.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-left.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-flow-right.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-long_int64.R
/usr/lib64/R/library/dotCall64/tests/testthat/test-vector_dc.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dotCall64/libs/dotCall64.so
/usr/lib64/R/library/dotCall64/libs/dotCall64.so.avx2
/usr/lib64/R/library/dotCall64/libs/dotCall64.so.avx512
