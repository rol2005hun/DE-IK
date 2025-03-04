///
/// Package to predict the possible countries of origin for a last name.
/// The current implementation uses the [nationalize.io](https://nationalize.io) web API.
///
/// Example of use:
/// ```java
/// var client = NationalizeClient.newInstance();
/// var nationality = client.getNationality("Lajos");
/// ```
package nationalize;