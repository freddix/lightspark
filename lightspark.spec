Summary:	Open source flash player
Name:		lightspark
Version:	0.7.0
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://edge.launchpad.net/lightspark/trunk/lightspark-%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	faa4d11aa3bd706c4644c634c5590949
URL:		http://lightspark.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	gettext
BuildRequires:	glew-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libav-devel
BuildRequires:	libtool
BuildRequires:	libxml++-devel
BuildRequires:	llvm-devel
BuildRequires:	nasm
BuildRequires:	pcre-cxx-devel
BuildRequires:	pcre-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	rtmpdump-devel
BuildRequires:	xulrunner-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_libdir}/browser-plugins

%description
Lightspark is a modern, free, open-source flash player implementation.

%package -n browser-plugin-%{name}
Summary:	Browser plugin for Flash rendering
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n browser-plugin-%{name}
Browser plugin for rendering Flash content using Lightspark.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DLIB_INSTALL_DIR=%{_lib}	\
	-DPLUGIN_DIRECTORY=%{plugindir} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/ldconfig
%update_icon_cache hicolor

%postun
/usr/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/lightspark
%attr(755,root,root) %{_bindir}/tightspark
%dir %{_libdir}/lightspark
%dir %{_libdir}/lightspark/plugins
%attr(755,root,root) %{_libdir}/lightspark/liblightspark.so.*.*
%attr(755,root,root) %{_libdir}/lightspark/liblightspark.so.*.*.*
%attr(755,root,root) %{_libdir}/lightspark/plugins/liblightsparkpulseplugin.so
%{_datadir}/lightspark
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/lightspark.png
%{_iconsdir}/hicolor/*/apps/lightspark.svg
%{_sysconfdir}/xdg/lightspark.conf
%{_mandir}/man1/lightspark.1*

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/liblightsparkplugin.so

