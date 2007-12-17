%define module	Acme-Cow
%define name	perl-%{module}
%define version 0.1
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A configurable speaking/thinking Cow
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.nog.net/~tony/warez/%{module}-%{version}.tar.bz2
Url:		http://www.nog.net/~tony/warez/cowsay.shtml
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Text::Template)
Buildarch:	noarch
conflicts:	cowsay

%description
Talking cows.  ASCII artwork.  A veritable foundation of the
Internet.

Now you can make the cows say whatever you want.  Acme::Cow is the
module that does all the work behind the new version of cow{say,think}
(also included in this distribution).  Now you can incorporate
loquactious cattle into any program you want, quickly and easily.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Acme*
%{_mandir}/*/*



