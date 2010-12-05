%define name enblend
%define version 3.2
%define rel 3
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tool for compositing images
Source0:	http://downloads.sourceforge.net/enblend/enblend-enfuse-%{version}.tar.gz
Patch0:		enblend-enfuse-3.1-cxxflags.patch
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
%if %mdkversion >= 200900
BuildRequires:  glew-devel
%endif
BuildRequires:  mesaglut-devel
BuildRequires:  lcms-devel
BuildRequires:  libxmi-devel
BuildRequires:	png-devel
BuildRequires:	ilmbase-devel
Provides:	enfuse = %version-%release

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep 
%setup -q -n enblend-enfuse-%{version}
%patch0 -p1 -b .cxxflags

#needed by patch0 
aclocal -I m4
autoconf 

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO VIGRA_LICENSE
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*
%{_infodir}/*
%{_bindir}/enblend
%{_bindir}/enfuse
