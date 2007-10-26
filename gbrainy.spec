Summary: A brain teaser game and trainer to have fun and to keep your brain trained
Name: gbrainy
Version: 0.3
Release: %mkrel 1
Source0: http://www.softcatala.org/~jmas/gbrainy/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/gbrainy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel

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
rm -fr %buildroot
%makeinstall_std
%find_lang %name

%clean
rm -fr %buildroot
