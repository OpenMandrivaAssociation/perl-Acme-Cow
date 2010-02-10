%define upstream_name	 Acme-Cow
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A configurable speaking/thinking Cow
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.nog.net/~tony/warez/cowsay.shtml
Source0:	http://www.nog.net/~tony/warez/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Text::Template)

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

conflicts:	cowsay

%description
Talking cows.  ASCII artwork.  A veritable foundation of the
Internet.

Now you can make the cows say whatever you want.  Acme::Cow is the
module that does all the work behind the new version of cow{say,think}
(also included in this distribution).  Now you can incorporate
loquactious cattle into any program you want, quickly and easily.

%prep
%setup -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Acme*
%{_mandir}/*/*
