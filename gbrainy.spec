%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A brain teaser game and trainer to have fun and to keep your brain trained
Name:		gbrainy
Version:	1.65
Release:	5
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/gbrainy
Source0:	http://gent.softcatala.org/jmas/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glade-sharp-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-sharp-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(mono-addins)

%description
gbrainy is a brain teaser game and trainer written for GNOME using Mono,
C# and Cairo.

Its mission is to provide a platform for creating different kinds of
brain-teasers and brain trainer games for GNOME.

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

#----------------------------------------------------------------------------

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

