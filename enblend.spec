Summary:	Tool for compositing images
Name:		enblend
Version:	4.2
Release:	3
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/enblend/enblend-enfuse/enblend-enfuse-%{version}/enblend-enfuse-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	help2man
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	vigra-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	texlive-pdftex.bin
BuildRequires:	texlive-latex.bin
BuildRequires:	texlive-kpathsea.bin
BuildRequires:	texlive-kpathsea
BuildRequires:	perl(DateTime::TimeZone)
Provides:	enfuse = %{version}-%{release}

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep
%autosetup -n enblend-enfuse-%{version} -p1
rm -f configure
%{__sed} -i -e 's/src:://g;s/CFG::/CFG_/g' configure.ac

%build
export CXX="%__cxx -std=c++11"
autoreconf -fiv
%configure --with-boost-filesystem --enable-openmp
%make_build

%install
%make_install

%files
%doc AUTHORS NEWS README
%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*

