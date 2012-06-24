%include	/usr/lib/rpm/macros.perl
Summary:	Support for compressed usenet feeds
Summary(pl):	Obs�uga feedu kompresowanych news�w
Name:		feeder
Version:	2.1.4
Release:	4
License:	GPL
Vendor:		feed-pl@egroups.com /subscription required or own server/
Group:		Applications/News
Source0:	http://newsy.media-com.com.pl/scripts2/%{name}-%{version}.tar.gz
Source1:	http://newsy.media-com.com.pl/scripts2/server-script/fetcher
URL:		http://newsy.media-com.com.pl/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of client scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver.

%description -l pl
Zestaw skrypt�w klienckich do �ci�gania i transferu do lokalnego
(proxy)newsserwera post�w w kompresowanych paczkach.

%package server
Summary:	Support for compressed usenet feeds - server side
Summary(pl):	Obs�uga feedu kompresowanych news�w - skrypt serwerowy
Requires:	perl-CGI
Group:		Applications/News

%description server
A set of server scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver.

%description server -l pl
Zestaw skrypt�w serwerowych do �ci�gania i transferu do lokalnego
(proxy)newsserwera post�w w kompresowanych paczkach i udost�pniania
ich klientom.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir} \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{perl_sitelib}/Feeder} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man{1,5,7} \
	$RPM_BUILD_ROOT%{_var}/spool/%{name}2/{archive,received}

install etc/feeder.conf $RPM_BUILD_ROOT%{_sysconfdir}
install usr/lib/perl5/site_perl/Feeder/feeder.pm $RPM_BUILD_ROOT%{perl_sitelib}/Feeder
install usr/local/bin/* $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}
install usr/local/share/man/pl/man1/* $RPM_BUILD_ROOT%{_mandir}/pl/man1
install usr/local/share/man/pl/man5/* $RPM_BUILD_ROOT%{_mandir}/pl/man5
install usr/local/share/man/pl/man7/* $RPM_BUILD_ROOT%{_mandir}/pl/man7
install var/spool/feeder2/* $RPM_BUILD_ROOT%{_var}/spool/%{name}2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Feeder
%attr(660,root,news) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
%attr(755,news,news) %dir %{_var}/spool/%{name}2
%attr(2775,news,news) %dir %{_var}/spool/%{name}2/archive
%attr(2775,news,news) %dir %{_var}/spool/%{name}2/received
%attr(664,news,news) %config(noreplace) %verify(not md5 size mtime) %{_var}/spool/%{name}2/groups
%attr(664,news,news) %config(noreplace) %verify(not md5 size mtime) %{_var}/spool/%{name}2/killfile
%lang(pl) %{_mandir}/pl/man?/*

%files server
%defattr(644,root,root,755)
%attr(755,news,news) %{_sbindir}/*
