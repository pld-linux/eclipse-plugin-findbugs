Summary:	FindBugs - plugin for Eclipse
Summary(pl):	FindBugs - wtyczka do ¶rodowiska Eclipse
Name:		eclipse-plugins-findbugs
%define	_date	20061006
Version:	1.1.1.%{_date}
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/findbugs/edu.umd.cs.findbugs.plugin.eclipse_%{version}.zip
# Source0-md5:	f7eea639cd7147522b78f81a11fba1de
URL:		http://findbugs.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_datadir}/eclipse

%description
FindBugs support for the Eclipse IDE Framework.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins/

cp -R *  $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*
