Summary:	Aqsis Rendering System
Summary(pl.UTF-8):	System Renderujący Aqsis
Name:		aqsis
Version:	1.2.0
Release:	3
License:	GPL v2 / LGPL v2.1
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aqsis/%{name}-%{version}.tar.gz
# Source0-md5:	ae9bb1c4b22e396fd7ce84ee3e13cb86
Patch0:		%{name}-scons-paths.patch
URL:		http://aqsis.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	bison >= 1.35
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	flex >= 2.5.4
BuildRequires:	fltk-devel >= 1.1.0
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.7.1
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 1.337
BuildRequires:	scons
BuildRequires:	zlib-devel >= 1.1.4
Provides:	renderman-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Aqsis Rendering System consists of a set of libraries and
applications for creating high-quality computer imagery using the
Pixar RenderMan Interface.

%description -l pl.UTF-8
System Renderujący Aqsis składa się z zestawu bibliotek i programów
do tworzenia wysokiej jakości obrazów komputerowych z użyciem
interfejsu RenderMan firmy Pixar.

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
Pliki nagłówkowe Systemu Renderującego Aqsis.

%prep
%setup -q
%patch0 -p1

sed -i -e "s#'lib'#'%{_lib}'#g" SConstruct
sed -i -e 's#/lib#/%{_lib}#g' platform/default/Options.py

%build
# We cannot build the targets here, because 'scons install' fires the entire
# compilation from the start.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/%{name},%{name},%{_bindir},%{_libdir},%{_datadir}/%{name},%{_examplesdir}}

export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcflags}'
export CC='%{__cc}'
export CFLAGS='%{rpmcflags}'
%scons \
	install_prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc/%{name} \
	pld_pluginsdir=%{_libdir}/%{name}/plugins \
	pld_shadersdir=%{_datadir}/%{name}/shaders \
	pld_configdir=/etc/%{name} \
	install
sed -e "s:$RPM_BUILD_ROOT::g" -i $RPM_BUILD_ROOT/etc/%{name}/aqsisrc
find $RPM_BUILD_ROOT -name '*.bat' -exec rm {} \;
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/content $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ReleaseNotes README
%dir /etc/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/%{name}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_datadir}/%{name}
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
