Summary:	Aqsis Rendering System
Summary(pl):	System renderuj±cy Aqsis
Name:		aqsis
Version:	0.9.2
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	db643748ebfbf7e14aa7f3b0fa2c143a
URL:		http://aqsis.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
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
System renderuj±cy Aqsis sk³ada siê z zestawu bibliotek i programów do
tworzenia wysokiej jako¶ci obrazów komputerowych z u¿yciem interfejsu
RenderMan firmy Pixar.

%package devel
Summary:	Header files for Aqsis Rendering System
Summary(pl):	Pliki nag³ówkowe systemu renderuj±cego Aqsis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libtiff-devel
Requires:	log4cpp-devel
Requires:	zlib-devel

%description devel
Header files for Aqsis Rendering System.

%description devel -l pl
Pliki nag³ówkowe systemu renderuj±cego Aqsis.

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
%{_datadir}/%{name}
%{_mandir}/man1/aqsis.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
