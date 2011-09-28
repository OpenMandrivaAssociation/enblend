Summary:	Tool for compositing images
Name:		enblend
Version:	4.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/enblend/enblend-enfuse/enblend-enfuse-%{version}/enblend-enfuse-%{version}.tar.gz
Patch0:		enblend-4.0-libpng14.patch
Patch1:		enblend-4.0-libpng15.patch
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
BuildRequires:	glew-devel
BuildRequires:	mesaglut-devel
BuildRequires:	lcms-devel
BuildRequires:	libxmi-devel
BuildRequires:	png-devel
BuildRequires:	ilmbase-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	perl(Time::Zone)
Provides:	enfuse = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep
%setup -q -n enblend-enfuse-4.0-753b534c819d
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README VIGRA_LICENSE
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*
%{_bindir}/enblend
%{_bindir}/enfuse
