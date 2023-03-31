%define _disable_ld_no_undefined 1

Summary:	X.org driver for Alliance Promotion
Name:		x11-driver-video-apm
Version:	1.3.0
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-apm-%{version}.tar.bz2

BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-apm is the X.org driver for Alliance Promotion.

%prep
%setup -qn xf86-video-apm-%{version}
%autopatch -p1

%build
%ifarch i586
export CC=gcc
%endif
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.*

