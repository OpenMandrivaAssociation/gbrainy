Summary: A brain teaser game and trainer to have fun and to keep your brain trained
Name: gbrainy
Version: 1.1
Release: %mkrel 2
Source0: http://www.softcatala.org/~jmas/gbrainy/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/gbrainy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: pkgconfig(glade-sharp-2.0)
BuildRequires: pkgconfig(gnome-sharp-2.0)
BuildRequires: pkgconfig(gtk-sharp-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: intltool

%description
gbrainy is a brain teaser game and trainer written for GNOME using Mono,
C# and Cairo. 

Its mission is to provide a platform for creating different kinds of
brain-teasers and brain trainer games for GNOME.

%prep
%setup -q -n%name-%version

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %name

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libexecdir}/%name/%name.exe
%{_libexecdir}/%name/%name.exe.config
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man6/*
%{_datadir}/pixmaps/*
%{_datadir}/games/%{name}
