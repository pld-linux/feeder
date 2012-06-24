%include	/usr/lib/rpm/macros.perl
Summary:	Support for compressed usenet feeds
Summary(pl):	Obs�uga feedu kompresowanych news�w
Name:		feeder
Version:	2.1.4
Release:	5
License:	GPL
Vendor:		feed-pl@egroups.com /subscription required or own server/
Group:		Applications/News
Source0:	http://newsy.media-com.com.pl/scripts2/%{name}-%{version}.tar.gz
Source1:	http://newsy.media-com.com.pl/scripts2/server-script/fetcher
# taken and rpm2cpioed from http://www.media-com.com.pl/~radecki/scripts/feeder-0.99-pre6.src.rpm
Source2:    feeder-0.99.tar.gz
Source3:    http://newsy.karnet.pl/sd
Source4:    http://newsy.karnet.pl/sd.conf
URL:		http://newsy.media-com.com.pl/
Patch0:     %{name}-0.99-url_n_notermcap.patch
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

%package old
Summary:    Support for compressed usenet feeds - old unauthorizing client
Summary(pl):    Obs�uga feedu kompresowanych news�w - stary nieautryzuj�cy si� klient
Requires:   perl
Group:      Applications/News

%description old
A set of client scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver, this one does not require
authorizing with server, but it only downloads articles, you need some
nttp utilities to post news. (rpost might be good start)

%description old -l pl
Zestaw skrypt�w klient�w do �ci�gania i transferu do lokalnego
newsserwera, skrypty te nie wymagaj� autoryzacji z serwerem news, ale 
nie umo�liwiaj� wysy�ania artyku��w, konieczne s� dodatkowe narz�dzia
aby wysy�a� artyku�y do zdalnych serwer�w. (rpost mo�e by� dobrym 
pocz�tkiem)

%package old-ppp
Summary:    Automagic get-news on ppp-up
Summary(pl):    Automagiczne pobieranie paczek po podniesieniu ppp
Group:      Applications/News
Requires:   /usr/bin/suckem_perl
Requires:   /usr/bin/feed2inn

%description old-ppp
This will automagicly fetch news after ppp-up.

%description old-ppp -l pl
Ten pakiet zautomagiczni �ci�gnanie paczek po po��czeniu ppp.

%prep
%setup -q -a2
echo $PWD
%patch -p0 

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/interfaces/up.d/ppp \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{perl_sitelib}/Feeder} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man{1,5,7} \
	$RPM_BUILD_ROOT%{_var}/spool/{%{name}2,%{name}}/{archive,received,old,tmp}
    

install etc/feeder.conf $RPM_BUILD_ROOT%{_sysconfdir}
install usr/lib/perl5/site_perl/Feeder/feeder.pm $RPM_BUILD_ROOT%{perl_sitelib}/Feeder
install usr/local/bin/* $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}
install usr/local/share/man/pl/man1/* $RPM_BUILD_ROOT%{_mandir}/pl/man1
install usr/local/share/man/pl/man5/* $RPM_BUILD_ROOT%{_mandir}/pl/man5
install usr/local/share/man/pl/man7/* $RPM_BUILD_ROOT%{_mandir}/pl/man7
install var/spool/feeder2/* $RPM_BUILD_ROOT%{_var}/spool/%{name}2

install %{name}-0.99/usr/bin/* $RPM_BUILD_ROOT%{_bindir}
install %{name}-0.99/var/spool/news/feeder/last $RPM_BUILD_ROOT%{_var}/spool/%{name}
install %{name}-0.99/var/spool/news/feeder/grupy $RPM_BUILD_ROOT%{_var}/spool/%{name}/groups

cat << EOF > $RPM_BUILD_ROOT/etc/sysconfig/interfaces/up.d/ppp/feeder
#!/bin/sh

( sleep 5
exec 3>&p
date |& mail news -s "feeder ppp-on, started on $(date)"
/usr/bin/suckem_perl -q 2>&1 >&p
/usr/bin/feed2inn -a 2>&1 >&p
date 2>&1 >&p
exec 3>&-
) &

EOF

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

%files old
%defattr(644,root,root,755)
%doc feeder-0.99/TODO
%attr(755,root,root) %{_bindir}/feed2inn
%attr(755,root,root) %{_bindir}/feed2slrnpull_a
%attr(755,root,root) %{_bindir}/feed2slrnpull_b
%attr(755,root,root) %{_bindir}/news.put
%attr(755,root,root) %{_bindir}/news.send
%attr(755,root,root) %{_bindir}/suckem_perl
%attr(755,root,root) %{_bindir}/suckem_sh
%attr(755,news,news) %dir %{_var}/spool/%{name}
%attr(2775,news,news) %dir %{_var}/spool/%{name}/old
%attr(2775,news,news) %dir %{_var}/spool/%{name}/received
%attr(2775,news,news) %dir %{_var}/spool/%{name}/tmp
%attr(664,news,news) %config(noreplace) %verify(not md5 size mtime) %{_var}/spool/%{name}/groups
%attr(664,news,news) %config(noreplace) %verify(not md5 size mtime) %{_var}/spool/%{name}/last
%lang(pl) %{_mandir}/pl/man?/*

%files old-ppp
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/interfaces/up.d/ppp/feeder
