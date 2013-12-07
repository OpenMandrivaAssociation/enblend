Summary:	Tool for compositing images
Name:		enblend
Version:	4.0
Release:	9
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/enblend/enblend-enfuse/enblend-enfuse-%{version}/enblend-enfuse-%{version}.tar.gz
Patch0:		enblend-4.0-libpng14.patch
Patch1:		enblend-4.0-libpng15.patch
Patch2:		enblend-4.0-boost-1.50.patch
Patch3:		enblend-4.0-boost-1.50-3.patch
BuildRequires:	boost-devel
BuildRequires:	libxmi-devel
BuildRequires:	tiff-devel
BuildRequires:	perl(Time::Zone)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(OpenEXR)
Provides:	enfuse = %{version}-%{release}

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep
%setup -q -n enblend-enfuse-4.0-753b534c819d
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%configure2_5x --with-boost-filesystem
sed -i s,"-lboost_filesystem","-lboost_filesystem -lboost_system",g src/Makefile
%make


%install
%makeinstall_std

%files
%doc AUTHORS NEWS README VIGRA_LICENSE
%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*

