%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Inner
Summary:	%{pdir}::%{pnam} - A perlish implementation of Java-like inner classes
Summary(pl):	%{pdir}::%{pnam} - perlowa implementacja wewnêtrznych klas w stylu Javy
Name:		perl-%{pdir}-%{pnam}
Version:	0.1
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another implementation of an anonymous class with per
object overrideable methods, but with the added attraction
of sort of working dispatch to the parent class's method.

# %description -l pl
# TODO, znów mnie przeros³a

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
