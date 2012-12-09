Name: x11-driver-video-apm
Version: 1.2.5
Release: 2
Summary: X.org driver for Alliance Promotion
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-apm-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-apm is the X.org driver for Alliance Promotion.

%prep
%setup -qn xf86-video-apm-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.5-1
+ Revision: 810729
- version update 1.2.5

* Tue May 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.4-1
+ Revision: 798909
- version update 1.2.4

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.3-7
+ Revision: 748368
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.3-6
+ Revision: 703645
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.3-5
+ Revision: 683559
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-4
+ Revision: 671138
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.3-3mdv2011.0
+ Revision: 595729
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sun Jul 25 2010 Thierry Vignaud <tv@mandriva.org> 1.2.3-1mdv2011.0
+ Revision: 558367
- new release

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-1mdv2010.0
+ Revision: 407730
- new release

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.1-1mdv2009.1
+ Revision: 317838
- New version 1.2.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 308210
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265900
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194217
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-7mdv2008.1
+ Revision: 165470
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-6mdv2008.1
+ Revision: 156596
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-5mdv2008.1
+ Revision: 154896
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  re only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-apm-1.1.1@mandriva suggested on upstream
  Tag at git checkout ca78b41a6fcb4110d8e19636baa8dfb4a9ef07bd
  There is already a tag named apm-1_1_1, but the local mandriva tag
  is probably a better option as it follows the pattern used by other
  repositories, and is newer than apm-1_1_1, including changes considered
  safe. To check the diff run:
  	git diff apm-1_1_1..xf86-video-apm-1.1.1@mandriva
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-4mdv2008.1
+ Revision: 98683
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2008.0
+ Revision: 75720
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

