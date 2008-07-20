%define name enblend
%define version 3.1
%define rel 2
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
Patch0:		enblend-enfuse-3.1-cxxflags.patch
License:	GPL
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


%changelog
* Wed May 28 2008 Nicholas Brown <nickbrown@mandriva.org> 3.1-0.20080528.1mdv2009.0
+ Revision: 212655
- cvs snapshot of 3.1
  remove patch merged upstream
  fix build dependancies for x86_64
  package enfuse
- New version

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.5-2mdv2008.1
+ Revision: 170813
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.5-1mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 13 2005 Lenny Cartier <lenny@mandriva.com> 2.5-1mdk
- 2.5

* Mon Dec 05 2005 Lenny Cartier <lenny@mandriva.com> 2.4-1mdk
- 2.4

* Mon Apr 18 2005 Lenny Cartier <lenny@mandriva.com> 2.3-1mdk
- 2.3

* Wed Dec 08 2004 Couriousous <couriousous@mandrake.org> 2.1-1mdk
- 2.1
- Update url
- Drop patch0

* Sun Jul 18 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.3-2mdk 
- Couriousous <couriousous@zarb.org> :
 - Added multilayer tiff support

* Wed Jun 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.3-1mdk
- contributed by Couriousous <couriousous@sceen.net>

