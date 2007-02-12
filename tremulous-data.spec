Summary:	Tremulous data files
Summary(pl.UTF-8):	Pliki danych dla Tremulous
Name:		tremulous-data
Version:	1.1.0
Release:	1
License:	Creative Commons
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/tremulous/tremulous-%{version}.zip
# Source0-md5:	3df5f7565571fb9524656308347bce1b
URL:		http://www.tremulous.net/
BuildRequires:	unzip
Requires:	tremulous-common = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tremulous data files.

%description -l pl.UTF-8
Pliki danych dla Tremulous.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/tremulous/base,%{_pixmapsdir}}

install tremulous/base/* $RPM_BUILD_ROOT%{_datadir}/games/tremulous/base

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tremulous/{CC,ChangeLog,COPYING,manual.pdf}
%{_datadir}/games/tremulous/base/*
