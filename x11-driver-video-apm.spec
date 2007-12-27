Name: x11-driver-video-apm
Version: 1.1.1
Release: %mkrel 5
Summary: The X.org driver for Alliance Promotion
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-apm-1.1.1@mandriva suggested on upstream
# Tag at git checkout ca78b41a6fcb4110d8e19636baa8dfb4a9ef07bd
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-apm  xorg/drivers/xf86-video-apm
# cd xorg/drivers/xf86-video/apm
# git-archive --format=tar --prefix=xf86-video-apm-1.1.1/  xf86-video-apm-1.1.1@mandriva | bzip2 -9 > xf86-video-apm-1.1.1.tar.bz2
########################################################################
Source0: xf86-video-apm-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch  xf86-video-apm-1.1.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Alliance Promotion

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-video-apm-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/*.la
%{_datadir}/X11/mandriva/*.deps
