# TODO:
# - Check to see if splitting plugins into several packages makes any sense
#   (probably not).
# - Check that everything works as expected.
# - Remove duplications in %files section.
# - Fix aqsis-scons-paths.patch so modyfing it after sysconfdir change will
#   not be needed.
# - Check why the second stage of compilation ignores CXX and CXXFLAGS and
#   fix it of course :)
# - Proper configuration files handling by SPEC.
# - Fix paths in configuration file.
Summary:	Aqsis Rendering System
Summary(pl.UTF-8):	System Renderujący Aqsis
Name:		aqsis
Version:	1.2.0
Release:	0.1
License:	GPL v2 / LGPL v2.1
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aqsis/%{name}-%{version}.tar.gz
# Source0-md5:	ae9bb1c4b22e396fd7ce84ee3e13cb86
Patch0:		aqsis-scons-paths.patch
URL:		http://aqsis.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	bison >= 1.35
BuildRequires:	boost-devel >= 1.32.0
BuildRequires:	flex >= 2.5.4
BuildRequires:	fltk-devel >= 1.1.0
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.7.1
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxslt-progs
BuildRequires:	zlib-devel >= 1.1.4
Provides:	renderman-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Aqsis Rendering System consists of a set of libraries and
applications for creating high-quality computer imagery using the
Pixar RenderMan Interface.

%description -l pl.UTF-8
System renderujący Aqsis składa się z zestawu bibliotek i programów do
tworzenia wysokiej jakości obrazów komputerowych z użyciem interfejsu
RenderMan firmy Pixar.

%package devel
Summary:	Header files for Aqsis Rendering System
Summary(pl.UTF-8):	Pliki nagłówkowe Systemu Renderującego Aqsis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libtiff-devel
Requires:	log4cpp-devel
Requires:	zlib-devel

%description devel
Header files for Aqsis Rendering System.

%description devel -l pl.UTF-8
Pliki nagłówkowe systemu renderującego Aqsis.

%prep
%setup -q
%patch0 -p1

%build
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcflags}'
export CC='%{__cc}'
export CFLAGS='%{rpmcflags}'
# WARNING! If you'll change the sysconfdir argument below, remember to
# make apriopriate change in aqsis-scons-paths.patch!
%{scons} \
	install_prefix="$RPM_BUILD_ROOT%{_prefix}" \
	sysconfdir="$RPM_BUILD_ROOT/etc/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/%{name},%{name},%{_bindir},%{_libdir},%{_datadir}/%{name}}

%{scons} install_prefix="$RPM_BUILD_ROOT%{_prefix}" install
#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la
#mv $RPM_BUILD_ROOT%{_usr}/etc $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ReleaseNotes README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so*
%dir %{_libdir}/%{name}/
%attr(755,root,root) %{_libdir}/%{name}/*.so
%dir %{_libdir}/%{name}/plugins/
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_libdir}/%{name}/lib*.so*
%{_datadir}/%{name}
/etc/%{name}

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/lib*.so
#%{_libdir}/lib*.la
%{_includedir}/%{name}
