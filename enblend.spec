Summary:	Tool for compositing images
Name:		enblend
Version:	4.0
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://enblend.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/enblend/enblend-enfuse/enblend-enfuse-%{version}/enblend-enfuse-%{version}.tar.gz
Patch0:		enblend-4.0-libpng14.patch
Patch1:		enblend-4.0-libpng15.patch
Patch2:		enblend-4.0-boost-1.50.patch
Patch3:		enblend-4.0-boost-1.50-3.patch
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	libxmi-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	perl(Time::Zone)
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
%{_mandir}/man1/enblend.1.*
%{_mandir}/man1/enfuse.1.*
%{_bindir}/enblend
%{_bindir}/enfuse


%changelog
* Thu Sep 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.0-2mdv2012.0
+ Revision: 701837
- add patches form gentoo to enable support for libpng15

* Sun May 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.0-1
+ Revision: 672529
- update to new version 4.0
- drop patch 0, not needed anymore
- add OpenEXR-devel and perl-Time-Zone to the buildrequires
- spec file clean

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2-3mdv2011.0
+ Revision: 610361
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 3.2-2mdv2009.1
+ Revision: 350332
- 2009.1 rebuild

* Thu Sep 11 2008 Funda Wang <fwang@mandriva.org> 3.2-1mdv2009.0
+ Revision: 283661
- New version 3.2 final
- add ilmbase-devel BR

* Sun Jul 20 2008 Frederic Crozat <fcrozat@mandriva.com> 3.1-0.20080528.2mdv2009.0
+ Revision: 239187
- Patch0: fix CXX flags used
- Disable GPU support when building for 2008.1 or older

* Wed May 28 2008 Nicholas Brown <nickbrown@mandriva.org> 3.1-0.20080528.1mdv2009.0
+ Revision: 212655
- cvs snapshot of 3.1
  remove patch merged upstream
  fix build dependancies for x86_64
  package enfuse
- New version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.5-2mdv2008.1
+ Revision: 170813
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.5-1mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
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

