Summary:	FindBugs - plugin for Eclipse
Summary(pl.UTF-8):	FindBugs - wtyczka do środowiska Eclipse
Name:		eclipse-plugins-findbugs
%define	_date	20061006
Version:	1.1.1.v%{_date}
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/findbugs/edu.umd.cs.findbugs.plugin.eclipse_%{version}.zip
# Source0-md5:	f081b2d991c4217330693e3216cc343d
URL:		http://findbugs.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_libdir}/eclipse

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
%{_eclipsedir}/plugins/*
