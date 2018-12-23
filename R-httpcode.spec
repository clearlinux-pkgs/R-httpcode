#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-httpcode
Version  : 0.2.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/httpcode_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/httpcode_0.2.0.tar.gz
Summary  : 'HTTP' Status Code Helper
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
Functions included for searching for codes by full or partial number,
    by message, and get appropriate dog and cat images for many
    status codes.

%prep
%setup -q -c -n httpcode

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530284003

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530284003
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpcode
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpcode
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpcode
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library httpcode|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/httpcode/DESCRIPTION
/usr/lib64/R/library/httpcode/INDEX
/usr/lib64/R/library/httpcode/LICENSE
/usr/lib64/R/library/httpcode/Meta/Rd.rds
/usr/lib64/R/library/httpcode/Meta/features.rds
/usr/lib64/R/library/httpcode/Meta/hsearch.rds
/usr/lib64/R/library/httpcode/Meta/links.rds
/usr/lib64/R/library/httpcode/Meta/nsInfo.rds
/usr/lib64/R/library/httpcode/Meta/package.rds
/usr/lib64/R/library/httpcode/NAMESPACE
/usr/lib64/R/library/httpcode/NEWS.md
/usr/lib64/R/library/httpcode/R/httpcode
/usr/lib64/R/library/httpcode/R/httpcode.rdb
/usr/lib64/R/library/httpcode/R/httpcode.rdx
/usr/lib64/R/library/httpcode/help/AnIndex
/usr/lib64/R/library/httpcode/help/aliases.rds
/usr/lib64/R/library/httpcode/help/httpcode.rdb
/usr/lib64/R/library/httpcode/help/httpcode.rdx
/usr/lib64/R/library/httpcode/help/paths.rds
/usr/lib64/R/library/httpcode/html/00Index.html
/usr/lib64/R/library/httpcode/html/R.css
