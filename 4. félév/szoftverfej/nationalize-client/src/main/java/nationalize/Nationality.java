package nationalize;

import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Stores the possible countries of origin for the last name.
 * @param count the number of rows examined
 * @param name last name for which the possible countries of origin should be predicted
 * @param countries a list of the most likely countries of origin
 */
public record Nationality(long count, String name, @SerializedName("country") List<Country> countries) {
    /**
     * Associates a probability with a country of origin.
     * @param countryId a two-letter country code
     * @param probability a number between 0 and 1
     */
    public record Country(String countryId, float probability) {}
}
