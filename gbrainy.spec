Summary:	A brain teaser game and trainer to have fun and to keep your brain trained
Name:		gbrainy
Version:	1.65
Release:	3
Source0:	http://gent.softcatala.org/jmas/%{name}/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/gbrainy
BuildRequires:	mono-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(glade-sharp-2.0)
BuildRequires:	pkgconfig(gnome-sharp-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	mono-addins-devel

%description
gbrainy is a brain teaser game and trainer written for GNOME using Mono,
C# and Cairo. 

Its mission is to provide a platform for creating different kinds of
brain-teasers and brain trainer games for GNOME.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# find_lang seems to fail on this
rm -rf %{buildroot}%{_datadir}/gnome/help/%{name}/sr@latin

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libexecdir}/%{name}/%{name}.exe
%{_libexecdir}/%{name}/%{name}.exe.config
%{_libexecdir}/%{name}/%{name}.Core.dll
%{_libexecdir}/%{name}/%{name}.Core.dll.config
%{_libexecdir}/%{name}/%{name}.Games.dll
%{_libdir}/pkgconfig/gbrainy.pc
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man6/*
%{_datadir}/pixmaps/*
%{_datadir}/games/%{name}


%changelog
* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 1.65-2mdv2012.0
+ Revision: 740995
- rebuild for gtk+ packaging breakage

* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 1.65-1
+ Revision: 652389
- New version 1.65

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 1.52-1mdv2011.0
+ Revision: 598535
- update to new version 1.52

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 1.51-2mdv2011.0
+ Revision: 584901
- rebuild

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 1.51-1mdv2011.0
+ Revision: 580730
- update to new version 1.51

* Tue Aug 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.50-1mdv2011.0
+ Revision: 572595
- fix source0
- remove post & postun (too old)
- update to 1.50

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 1.42-1mdv2011.0
+ Revision: 554673
- update to new version 1.42

* Fri Apr 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.41-1mdv2010.1
+ Revision: 535368
- up to 1.41

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 1.40-1mdv2010.1
+ Revision: 513157
- Update to new version 1.40

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.30-1mdv2010.1
+ Revision: 504505
- BR gnome-doc-utils
- new version 1.30

* Thu Nov 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.20-1mdv2010.1
+ Revision: 465275
- update to new version 1.20

* Sat Aug 22 2009 Frederik Himpe <fhimpe@mandriva.org> 1.12-1mdv2010.0
+ Revision: 419737
- update to new version 1.12

* Sun Jun 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.11-1mdv2010.0
+ Revision: 385900
- update to new version 1.11

* Sat Mar 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1-2mdv2009.1
+ Revision: 354880
- BuildRequires mono-addins
- Update to new version 1.1

* Fri Dec 26 2008 Frederik Himpe <fhimpe@mandriva.org> 1.01-1mdv2009.1
+ Revision: 319318
- Fix BuildRequires
- update to new version 1.01

* Wed Sep 03 2008 Funda Wang <fwang@mandriva.org> 1.00-2mdv2009.0
+ Revision: 279411
- fix file list

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 1.00-1mdv2009.0
+ Revision: 278651
- Fix BuildRequires
- Update to version 1.00, adding config file to file list

* Fri Aug 22 2008 Funda Wang <fwang@mandriva.org> 0.70-2mdv2009.0
+ Revision: 275022
- rebuild
- fix br in order to backport

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 0.70-1mdv2009.0
+ Revision: 227757
- update to new version 0.70

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 15 2008 Funda Wang <fwang@mandriva.org> 0.61-1mdv2009.0
+ Revision: 193655
- BR gnome-sharp2-devel
- New version 0.61

* Sat Mar 08 2008 Funda Wang <fwang@mandriva.org> 0.60-1mdv2008.1
+ Revision: 182089
- New version 0.60

* Sun Feb 24 2008 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 174264
- New version 0.53

* Fri Feb 08 2008 Funda Wang <fwang@mandriva.org> 0.5.2-1mdv2008.1
+ Revision: 164029
- New version 0.52

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 0.5.1-1mdv2008.1
+ Revision: 158577
- add missing file
- New version 0.51

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 111010
- fix file list
- drop patch0
- New version 0.41

* Fri Nov 09 2007 Funda Wang <fwang@mandriva.org> 3mdv2008.1-current
+ Revision: 107078
- rebuild for new lzma

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 102721
- fix startup script (bug#35093)

* Fri Oct 26 2007 Funda Wang <fwang@mandriva.org> 0.3-1mdv2008.1
+ Revision: 102284
- More BR
- add filelist
- Import gbrainy
- create gbrainy

