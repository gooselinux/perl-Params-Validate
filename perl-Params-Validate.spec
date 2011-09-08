Summary: 	Params-Validate Perl module
Name: 		perl-Params-Validate
Version: 	0.92
Release: 	3%{?dist}
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Params-Validate/
Source0: 	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Pod::Man)
# N/A in Fedora: BuildRequires:  perl(Module::Build) >= 0.35
BuildRequires:  perl(Module::Build)

# Required by the tests
BuildRequires: 	perl(Test::Taint)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Readonly::XS)

# For improved tests
#BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)

%description
The Params::Validate module allows you to validate method or function
call parameters to an arbitrary level of specificity. At the simplest
level, it is capable of validating the required parameters were given
and that no unspecified additional parameters were passed in. It is
also capable of determining that a parameter is of a specific type,
that it is an object of a certain class hierarchy, that it possesses
certain methods, or applying validation callbacks to arguments.

%prep
%setup -q -n Params-Validate-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} $RPM_BUILD_ROOT/*


%clean
rm -rf $RPM_BUILD_ROOT

%check
%if "%{version}" > "0.92"
IS_MAINTAINER=1 ./Build test
%else
# we don't have Test::Kwalitee here
rm -rf t/kwalitee.t
./Build test
%endif

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README TODO
%{perl_vendorarch}/Params
%{perl_vendorarch}/auto/Params
%{perl_vendorarch}/Attribute
%{_mandir}/man3/*

%changelog
* Fri Jan 15 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.92-3
- switch off Kwalitee tests, which we don't provide
- Resolves: rhbz#553449

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.92-2
- rebuild against perl 5.10.1

* Mon Nov 23 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.92-1
- Upstream update.
- Switch to Build.PL.
- Disable IS_MAINTAINER test.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 10 2008 Ralf Corsépius <rc040203@freenet.de> - 0.91-1
- Upstream update.
- Conditionally activate IS_MAINTAINER tests.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.89-4
- Rebuild for perl 5.10 (again)

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 0.89-3
- Rebuild for gcc43.

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.89-2
- rebuild for new perl

* Tue Nov 13 2007 Ralf Corsépius <rc040203@freenet.de> - 0.89-1
- Upstream update.

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 0.88-3
- Update license tag.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 0.88-2
- Mass rebuild.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 0.88-1
- BR: perl(ExtUtils::MakeMaker).
- Upstream update.

* Sat Jan 20 2007 Ralf Corsépius <rc040203@freenet.de> - 0.87-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.86-2
- Mass rebuild.

* Sun Aug 13 2006 Ralf Corsépius <rc040203@freenet.de> - 0.86-1
- Upstream update.

* Mon Jun 28 2006 Ralf Corsépius <rc040203@freenet.de> - 0.85-1
- Upstream update.

* Mon Jun 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.84-1
- Upstream update.

* Sun May 21 2006 Ralf Corsépius <rc040203@freenet.de> - 0.82-1
- Upstream update.

* Wed Apr 04 2006 Ralf Corsépius <rc040203@freenet.de> - 0.81-1
- Upstream update.

* Wed Feb 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.80-2
- Rebuild.

* Wed Feb 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.80-1
- Upstream update.

* Sat Jan 14 2006 Ralf Corsépius <rc040203@freenet.de> - 0.79-1
- Upstream update.
- BR perl(Readonly), perl(Readonly::XS).

* Sun Aug 14 2005 Ralf Corsepius <ralf@links2linux.de> - 0.78-2
- Spec file cleanup.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.78-1
- FE submission.
