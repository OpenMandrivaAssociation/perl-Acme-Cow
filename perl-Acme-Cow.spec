%define upstream_name	 Acme-Cow
%define upstream_version 0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A configurable speaking/thinking Cow
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://www.nog.net/~tony/warez/cowsay.shtml
Source0:	http://www.nog.net/~tony/warez/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Template)

BuildArch:	noarch

Conflicts:	cowsay

%description
Talking cows.  ASCII artwork.  A veritable foundation of the
Internet.

Now you can make the cows say whatever you want.  Acme::Cow is the
module that does all the work behind the new version of cow{say,think}
(also included in this distribution).  Now you can incorporate
loquactious cattle into any program you want, quickly and easily.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files 
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Acme*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680441
- mass rebuild

* Wed Feb 10 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 503910
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-11mdv2010.0
+ Revision: 430255
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.1-10mdv2009.0
+ Revision: 255254
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-8mdv2008.1
+ Revision: 133627
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.1-7mdv2007.0
+ Revision: 73165
- import perl-Acme-Cow-0.1-7mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-7mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1-6mdk
- Buildrequires fix using perl policy

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.1-5mdk
- Buildrequires fix

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-4mdk 
- better url
- drop useless empty directories
- spec cleanup
- rpmbuildupdate aware
- make test (even cows have regression tests)

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-3mdk
- fix buildrequires in a backward compatible way

* Sun Jun 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-2mdk 
- mooooooooooooooooo! (aka fixing changelog, thx Stefan <stefan@eijk.nu>)

* Sun Jun 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-1mdk 
- yeeeeeeeeeeeeeeeeeeeeeeeeeeeah

