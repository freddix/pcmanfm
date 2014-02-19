Summary:	Lightweight GTK+ file manager
Name:		pcmanfm
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
# Source0-md5:	11d59a492c9802866279a6e7e2b3f49e
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
Requires:	libfm-runtime >= 1.2.0
Requires:	shared-mime-info
Requires:	xdg-icon-theme
Suggests:	gvfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCManFM is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gtk=2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/tt_RU

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/pcmanfm
%dir %{_sysconfdir}/xdg/pcmanfm
%dir %{_sysconfdir}/xdg/pcmanfm/default
%{_sysconfdir}/xdg/pcmanfm/default/pcmanfm.conf
%{_datadir}/pcmanfm
%{_desktopdir}/pcmanfm.desktop
%{_desktopdir}/pcmanfm-desktop-pref.desktop
%{_mandir}/man1/pcmanfm.1*

