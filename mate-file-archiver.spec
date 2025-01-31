%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	An archive manager for MATE
Name:		mate-file-archiver
Version:	1.4.1
Release:	1
License:	GPLv2+
URL:		https://mate-desktop.org
Group:		Archiving/Compression
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	xsltproc
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(sm)

Suggests:	cdrecord-isotools
#Requires:	packagekit-gui
Requires(pre):	mate-conf
# for the gsettings schema
Requires:	mate-file-manager

%description
Emgrampa is an archive manager for the MATE environment.  This means that 
you can : create and modify archives; view the content of an archive; view a 
file contained in the archive; extract files from the archive.
Emgrampa is only a front-end (a graphical interface) to archiving programs 
like tar and zip. The supported file types are :
	* Tar archives uncompressed (.tar) or compressed with
		* gzip (.tar.gz , .tgz)
		* bzip (.tar.bz , .tbz)
		* bzip2 (.tar.bz2 , .tbz2)
		* compress (.tar.Z , .taz)
		* lzop (.tar.lzo , .tzo)
	* lzma (.tar.lzma , .tlz)
	* Zip archives (.zip)
	* Jar archives (.jar , .ear , .war)
	* Lha archives (.lzh)
	* Rar archives (.rar)
	* Single files compressed with gzip, bzip, bzip2, compress, lzop, lzma
	* ISO images

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-packagekit \
	--enable-caja-actions

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README 
%{_sysconfdir}/mateconf/schemas/engrampa.schemas
%{_bindir}/*
%{_libdir}/caja/extensions-2.0/*.so
%{_libexecdir}/engrampa
%{_datadir}/applications/*
%{_datadir}/engrampa
%{_iconsdir}/hicolor/*/*/*.*

