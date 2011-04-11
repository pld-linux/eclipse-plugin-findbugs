Summary:	FindBugs - plugin for Eclipse
Summary(pl.UTF-8):	FindBugs - wtyczka do środowiska Eclipse
Name:		eclipse-plugins-findbugs
%define	_date	20090821
Version:	1.3.9.%{_date}
Release:	2
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/findbugs/edu.umd.cs.findbugs.plugin.eclipse_%{version}.zip
# Source0-md5:	89d086d318ef110fc4af8bfc63f19ad1
URL:		http://findbugs.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.6
Requires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_libdir}/eclipse/dropins/findbugs

%description
FindBugs support for the Eclipse IDE Framework.

%description -l pl.UTF-8
Obsługa FindBugs dla środowiska programistycznego Eclipse.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

cp -R * $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/*
