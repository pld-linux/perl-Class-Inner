#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Inner
Summary:	Class::Inner - a perlish implementation of Java-like inner classes
Summary(pl):	Class::Inner - perlowa implementacja wewnêtrznych klas w stylu Javy
Name:		perl-Class-Inner
Version:	0.1
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	388db813c6a7050c4e0483bc4d86fc21
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another implementation of an anonymous class with per object
overrideable methods, but with the added attraction of sort of
working dispatch to the parent class's method.

%description -l pl
Jeszcze jedna implementacja anonimowej klasy z metodami przykrywalnymi
dla obiektu, ale z dodanym czym¶ w rodzaju wysy³ania do metody klasy
nadrzêdnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
