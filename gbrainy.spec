%define realver 0.41
Summary: A brain teaser game and trainer to have fun and to keep your brain trained
Name: gbrainy
Version: 0.4.1
Release: %mkrel 1
Source0: http://www.softcatala.org/~jmas/gbrainy/%{name}-%{realver}.tar.gz
Patch0: gbrainy-0.3-fix-startup-wrapper.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/gbrainy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: gnome-sharp2 gtk-sharp2-devel glade-sharp2

%description
gbrainy is a brain teaser game and trainer written for GNOME using Mono,
C# and Cairo. 

Its mission is to provide a platform for creating different kinds of
brain-teasers and brain trainer games for GNOME.

%prep
%setup -q -n%name-%realver
%patch0 -p0 

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %name

%clean
rm -fr %buildroot

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,-,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
