Summary:	Lightweight GTK+ file manager
Name:		pcmanfm
Version:	1.0.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	f373ee514bae37b53b152d02ac465058
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libfm-devel
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
Requires:	libfm-runtime
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
	--enable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{no,sv_SE,tt_RU,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

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

