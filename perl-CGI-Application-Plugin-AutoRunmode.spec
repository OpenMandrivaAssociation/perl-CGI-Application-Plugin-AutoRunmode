%define module   CGI-Application-Plugin-AutoRunmode
%define version    0.16
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    CGI::App plugin to automatically register runmodes
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
BuildRequires: perl(CGI::Application)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin for CGI::Application provides easy ways to setup run modes. You
can just write the method that implement a run mode, you do not have to
explicitly register it with CGI::App anymore.

There are two approaches: 

* Declare run modes with subroutine attributes. 

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


