Summary:	Wrapper library for reading or writing gzip/bzip2/lzma/xz files
Summary(pl.UTF-8):	Biblioteka pośrednia do odczytu i zapisu plików gzip/bzip2/lzma/xz
Name:		libzio
Version:	1.09
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/libzio/%{name}-%{version}.tar.bz2
# Source0-md5:	3fb6f31b7c9868b3741fae6ed9ebf3f0
Patch0:		%{name}-zstd.patch
URL:		https://libzio.sourceforge.net/
BuildRequires:	bzip2-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small library provides with the help of the fopencookie(3) of the
glibc and the libz, libbz2 and libzma a simple interface for reading
or writing gzip/bzip2/lzma/xz files.

%description -l pl.UTF-8
Ta mała biblioteka przy pomocy funkcji fopencookie(3) z glibc i
bibliotek libz/libbz2/liblzma dostarcza prosty interfejs do odczytu i
zapisu plików gzip/bzip2/lzma/xz.

%package devel
Summary:	Header files for libzio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libzio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libzio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libzio.

%package static
Summary:	Static libzio library
Summary(pl.UTF-8):	Statyczna biblioteka libzio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libzio library.

%description static -l pl.UTF-8
Statyczna biblioteka libzio.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libzio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libzio.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzio.so
%{_includedir}/zio.h
%{_mandir}/man3/fzopen.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libzio.a
