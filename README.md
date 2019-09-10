# Unsplash-HD-image-downloading-GUI-application
# Hey guys,
# why you should use this cause:
  * This will save you time.
  * It will find you photos what type of you need in a short time.
  * It is free of cost.
  * It's easy to use.
  * Life time runing.
# Set up API in application
  * Just go [this](https://unsplash.com/developers) website, resister as a developer.
  * Get API from there
  * Read [documentation](https://unsplash.com/documentation) if you like otherwise you can skip.
  * Paste API at the place `{your API key}`
# Quick set up guide:
  1. Location
      * The API is available at `https://api.unsplash.com/`. Responses are sent as `JSON.`
  2. Public Actions
      * Many actions can be performed without requiring authentication from a specific user. For example, `downloading a photo does not require a user to log in.`

      * To authenticate requests in this way, pass your application’s access key via the `HTTP Authorization header:`

  3. Authorization: `Client-ID YOUR_ACCESS_KEY`
      * You can also pass this value using a `client_id query` parameter:
         `https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY`
      If only your access key is sent, attempting to perform non-public actions that require user authorization will result in a `401` Unauthorized response.
   4. Link
      URL’s for the first, last, next, and previous pages are supplied, if applicable. They are comma-separated and differentiated with a rel attribute.

      1. For example, after requesting page 3 of the photo list:
          **`Link: <https://api.unsplash.com/photos?page=1>; rel="first",`
         *`<https://api.unsplash.com/photos?page=2>; rel="prev",`
         *`<https://api.unsplash.com/photos?page=346>; rel="last",`
         *`<https://api.unsplash.com/photos?page=4>; rel="next"`
 # Full Url set up
    (api = f'https://api.unsplash.com/photos/search?query={image_name}&resolution={size}&orientation={orientation}&client_id={Your API Key} ={pages}&w=1500&dpi=2)
    
    `pixel size : 1500, 1080, 400, 200`

   5. Supported parameters
      * We officially support the parameters:
       * `w, h:` for adjusting the width and height of a photo.
       * `crop:` for applying cropping to the photo.
       * `fm:` for converting image format.
       * `auto=format:` for automatically choosing the optimal image format depending on user browser.
       * `q:` for changing the compression quality when using lossy file formats.
       * `fit:` for changing the fit of the image within the specified dimensions.
       * `dpi:` for adjusting the device pixel ratio of the image.
  
# Search by key words [Doc](https://unsplash.com/documentation#search-photos)
  1. Parameters
       * `query`	Search terms.
       * `page`	Page number to retrieve. `(Optional; default: 1)`
       * `per_page`	Number of items per page. `(Optional; default: 10)`
       * `collections`	Collection ID(‘s) to narrow search. If multiple, comma-separated.
       * `orientation`	Filter search results by photo orientation. Valid values are landscape, portrait, and squarish.
  2. Response
       * The photo objects returned here are abbreviated. For full details use `GET /photos/:id`
       `200 OK
        Link: <https://api.unsplash.com/search/photos?page=1&query=office>; rel="first", <https://api.unsplash.com/search/photos?          page=1&query=office>; rel="prev", <https://api.unsplash.com/search/photos?page=3&query=office>; rel="last",https://api.unsplash.com/search/photos?page=3&query=office>; rel="next" X-Ratelimit-Limit: 1000
X-Ratelimit-Remaining: 999`

# Random photos
  1. Get a random photo
      1. Retrieve a single random photo, given optional filters.

  2. GET /photos/random
      1. Note: See the note on hotlinking.

  3. Parameters
      1. All parameters are optional, and can be combined to narrow the pool of photos from which a random one will be chosen.

  4. param	Description
      1. `collections`	Public collection `ID(‘s)` to filter selection. If multiple, comma-separated
      2. `featured`	Limit selection to featured photos.
      3. `username`	Limit selection to a single user.
      4. `query`	Limit selection to photos matching a search term.
      5. `orientation`	Filter search results by photo orientation. Valid values are `landscape`, `portrait`, and `squarish.`
      6. `count`	The number of photos to return. `(Default: 1; max: 30)`
# Uses of my application
  * use commercial.
  * use Non-commercial it up to you.
  * you can user profesionaly and perosonal use.
# Keep sporting and loving all of you guys.
# Have a nice day.
