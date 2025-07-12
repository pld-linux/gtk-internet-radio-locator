Summary:	GTK Internet Radio Locator (GTK 4 version)
Summary(pl.UTF-8):	GTK Internet Radio Locator (wersja dla GTK 4) - program do wyszukiwania rozgłośni internetowych
Name:		gtk-internet-radio-locator
Version:	4.8.3
Release:	2
License:	GPL v3+ (parts LGPL v2.1+ or GPL v2+)
Group:		X11/Applications/Sound
Source0:	https://download.gnome.org/sources/gtk-internet-radio-locator/4.8/%{name}-%{version}.tar.xz
# Source0-md5:	04dc0f4ff9894009ac54fd0eb35386ff
URL:		https://wiki.gnome.org/Apps/Girl
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.11
BuildRequires:	geocode-glib-devel >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0
# pkgconfig(gstreamer-player-1.0)
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk4-devel >= 4.9.2
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:0.28
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	geocode-glib >= 3.20
Requires:	glib2 >= 1:2.38.0
Requires:	gtk4 >= 4.9.2
Requires:	libchamplain >= 0.12.10
# only functionally, both packages can be installed simultaneously
#Obsoletes:	girl
#Obsoletes:	gnome-internet-radio-locator
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Internet Radio Locator program, allows users to easily find live
radio programs on radio broadcasters on the Internet.

%description -l pl.UTF-8
GTK Internet Radio Locator to program pozwalający użytkownikom łatwo
wyszukać programy internetowych rozgłości radiowych nadających na
żywo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-recording
# --with-help is broken

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BROADCAST ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gtk-internet-radio-locator
%{_datadir}/gtk-internet-radio-locator
%{_datadir}/appdata/gtk-internet-radio-locator.appdata.xml
%{_desktopdir}/gtk-internet-radio-locator.desktop
%{_iconsdir}/hicolor/*x*/apps/gtk-internet-radio-locator.png
%{_mandir}/man1/gtk-internet-radio-locator.1*
