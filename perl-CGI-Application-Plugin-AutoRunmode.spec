%define upstream_name    CGI-Application-Plugin-AutoRunmode
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	CGI::App plugin to automatically register runmodes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildArch:	noarch

%description
This plugin for CGI::Application provides easy ways to setup run modes. You
can just write the method that implement a run mode, you do not have to
explicitly register it with CGI::App anymore.

There are two approaches: 

* Declare run modes with subroutine attributes. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 657389
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1
+ Revision: 638894
- update to new version 0.18

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 553573
- update to 0.17

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 405772
- rebuild using %%perl_convert_version

* Sun Feb 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 340551
- update to new version 0.16

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 291351
- import perl-CGI-Application-Plugin-AutoRunmode


* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
- initial mdv release, generated with cpan2dist

