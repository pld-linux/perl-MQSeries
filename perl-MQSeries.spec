#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MQSeries
%define	pnam	MQSeries
Summary:	Perl extension for MQSeries support
Summary(pl):	Rozszerzenia Perla o obs³ugê MQSeries
Name:		perl-MQSeries
Version:	1.20
Release:	0.1
License:	custom, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e62bf783f62138e9698c3f8a164f7596
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for MQSeries support.

%description -l pl
Rozszerzenia Perla o obs³ugê MQSeries.

%prep
%setup -q -n %{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
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
%doc Changes README LICENSE
# use macros:
#%%{perl_vendorlib}/...
#%%{perl_vendorarch}/...
%{_mandir}/man3/*
