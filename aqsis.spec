Summary:	Aqsis Rendering System
Summary(pl):	System renderuj�cy Aqsis
Name:		aqsis
Version:	1.0.1
Release:	1
License:	GPL v2 / LGPL v2.1
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aqsis/%{name}-%{version}.tar.gz
# Source0-md5:	17e58818ab647f002c642c8abe591e35
URL:		http://aqsis.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	log4cpp-devel
BuildRequires:	zlib-devel
Provides:	renderman-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Aqsis Rendering System consists of a set of libraries and
applications for creating high-quality computer imagery using the
Pixar RenderMan Interface.

%description -l pl
System renderuj�cy Aqsis sk�ada si� z zestawu bibliotek i program�w do
tworzenia wysokiej jako�ci obraz�w komputerowych z u�yciem interfejsu
RenderMan firmy Pixar.

%package devel
Summary:	Header files for Aqsis Rendering System
Summary(pl):	Pliki nag��wkowe systemu renderuj�cego Aqsis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libtiff-devel
Requires:	log4cpp-devel
Requires:	zlib-devel

%description devel
Header files for Aqsis Rendering System.

%description devel -l pl
Pliki nag��wkowe systemu renderuj�cego Aqsis.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/displays.ini
%{_datadir}/%{name}
%{_mandir}/man1/aqsis.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
