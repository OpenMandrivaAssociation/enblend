%define name enblend
%define version 3.1
%define rel 1
%define cvs 20080528
%define release %mkrel 0.%{cvs}.%{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tool for compositing images
# The source for this package was pulled from upstream's CVS.  Use the
# following commands to generate the tarball:
#  cvs -d:pserver:anonymous@enblend.cvs.sourceforge.net:/cvsroot/enblend login 
#  cvs -z3 -d:pserver:anonymous@enblend.cvs.sourceforge.net:/cvsroot/enblend co -D '2008-05-28 21:00:00' -P enblend
#  cd enblend && make -f Makefile.cvs && ./configure && make dist
Source0:	enblend-enfuse-%{version}.tar.bz2
License:	GPL
Group:		Graphics
Url:		http://enblend.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
BuildRequires:  glew-devel
BuildRequires:  mesaglut-devel
BuildRequires:  lcms-devel
BuildRequires:  libxmi-devel
BuildRequires:	png-devel

%description
Enblend is a tool for compositing images. Given a set of images that overlap 
in some irregular way, Enblend overlays them in such a way that the seam 
between the images is invisible, or at least very difficult to see.

%prep 
%setup -q -n enblend-enfuse-%{version}

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
%doc AUTHORS COPYING NEWS README TODO VIGRA_LICENSE
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*
%{_bindir}/enblend
%{_bindir}/enfuse
