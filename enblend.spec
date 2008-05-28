%define name enblend
%define version 3.0
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tool for compositing images
Source0:	%{name}-%{version}.tar.bz2
Patch:		enblend-gcc43.patch
License:	GPL
Group:		Graphics
Url:		http://enblend.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:	libtiff-devel
BuildRequires:  libglew-devel
BuildRequires:  libmesaglut-devel
BuildRequires:  liblcms-devel
BuildRequires:  libxmi-devel

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep 
%setup -q
%patch -p1 -b .gcc43

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_mandir}/man1/enblend.1.*
%{_bindir}/enblend

