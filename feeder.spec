%include	/usr/lib/rpm/macros.perl
Summary:	Support for compressed usenet feeds
Summary(pl):	Obs�uga feedu kompresowanych news�w
Name:		feeder
Version:	2.1.3
Release:	3
License:	GPL
Vendor:		feed-pl@egroups.com /subscription required/
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://newsy.media-com.com.pl/scripts2/%{name}-%{version}.tar.gz
URL:		http://newsy.media-com.com.pl/
BuildRequires:	perl-devel
BuildRequires:	perl-News-NNTPClient
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of client scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver.

%description -l pl
Zestaw skrypt�w klienckich do �ci�gania i transferu do lokalnego
news(proxy)serwera post�w w kompresowanych paczkach.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir} \
	$RPM_BUILD_ROOT{%{_bindir},%{perl_sitelib}/Feeder} \
	$RPM_BUILD_ROOT{%{_mandir}/pl/man{1,5,7},%{_var}/spool/%{name}2}

%{__install} etc/feeder.conf $RPM_BUILD_ROOT%{_sysconfdir}
%{__install} usr/lib/perl5/site_perl/Feeder/feeder.pm $RPM_BUILD_ROOT%{perl_sitelib}/Feeder
%{__install} usr/local/bin/* $RPM_BUILD_ROOT%{_bindir}
%{__install} usr/local/share/man/pl/man1/* $RPM_BUILD_ROOT%{_mandir}/pl/man1
%{__install} usr/local/share/man/pl/man5/* $RPM_BUILD_ROOT%{_mandir}/pl/man5
%{__install} usr/local/share/man/pl/man7/* $RPM_BUILD_ROOT%{_mandir}/pl/man7
%{__install} var/spool/feeder2/* $RPM_BUILD_ROOT%{_var}/spool/%{name}2

%{__gzip} -9nf ChangeLog README

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Feeder
%attr(660,root,news) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
%attr(755,news,news) %dir %{_var}/spool/%{name}2
%attr(664,news,news) %config(noreplace) %verify(not md5 size mtime) %{_var}/spool/%{name}2/*
%lang(pl) %{_mandir}/pl/man?/*
