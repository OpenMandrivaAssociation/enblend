Summary:	Tool for compositing images
Name:		enblend
Version:	4.1.2
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/enblend/enblend-enfuse/enblend-enfuse-%{version}/enblend-enfuse-%{version}.tar.gz
Patch0:		enblend-enfuse-4.1.1-texinfo.patch
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	vigra-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(OpenEXR)
Provides:	enfuse = %{version}-%{release}

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep
%setup -q -n enblend-enfuse-%{version}
%apply_patches
%{__sed} -i -e 's/src:://g;s/CFG::/CFG_/g' doc/*.texi doc/define2set.pl configure.in

%build
autoreconf -fiv
%configure2_5x --with-boost-filesystem
%make


%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*

