# TODO:
#	- fix relinking of libaqsis.so.0.0 !!!
#	- break into subpackages

Summary:	Aqsis Rendering System
Summary(pl):	System renderuj±cy Aqsis
Name:		aqsis
Version:	0.9.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c4b3bb773f2016d24ec5659b43fa50cf
URL:		http://aqsis.sourceforge.net/
BuildRequires:	log4cpp-devel
Provides:	renderman-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Aqsis Rendering System consists of a set of libraries and applications 
for creating high-quality computer imagery using the Pixar RenderMan Interface.

%description -l pl
System renderuj±cy Aqsis sk³ada siê z zestawu bibliotek i programów do tworzenia
wysokiej jako¶ci obrazów komputerowych u¿ywaj±c interfejsu RenderMan firmy Pixar.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-log4cpptest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/lib*
%{_libdir}/%{name}
%{_sysconfdir}/*
